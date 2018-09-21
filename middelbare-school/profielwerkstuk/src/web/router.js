/**
 * De router.
 * Een router-bestand bevat de verschillende routes op onze web server.
 * In dit bestand staan dus al deze routes beschreven.
 */

const { inspect } = require('util');
const { log } = require(`${__dirname}/../utils`);

// De route voor gebruikers profielen, b.v. /users/zain_ali
exports.userProfile = async function userProfile (app, { login, posts }) {
  app.get('/users/:username', async (req, res) => {
    const profile = await login.getProfile(req.params.username);
    if (!profile) {
      return res.render('error', {
        title: 'Deze gebruiker is niet gevonden.',
        subtitle: 'Klik hier om terug te gaan naar de home pagina.',
        href: '/'
      });
    }

    const token = req.session.token;
    const credentials = await login.authenticate(token);

    const userPosts = await posts.getAll()
      .then(posts => posts.filter(post => post.author.toLowerCase() === profile.username.toLowerCase()));

    res.render('profile', { profile, credentials, posts: userPosts });
  });
};

// De route voor het maken van een post. Deze route is "intern" en wordt niet bezocht door gebruikers.
exports.createPost = async function createPost (app, { login, posts }) {
  app.post('/createPost', async (req, res) => {
    req.headers.Authorization = req.headers.Authorization || req.session.token;

    if (!req.headers.Authorization) {
      return res.status(401).send('Missing Authorization header');
    }

    if (!req.body.title || !req.body.content) {
      return res.status(400).send('Missing title or content');
    }

    const credentials = await login.authenticate(req.headers.Authorization);
    if (!credentials) {
      return res.status(401).send('Invalid Authorization header');
    }

    const post = await posts.create({
      title: req.body.title,
      content: req.body.content,
      author: credentials.username,
      categories: req.body.categories
    });

    res.redirect(`/posts/${post.insertedId}`);
  });
};

// Op deze route zie je een bepaalde post, bijvoorbeeld /posts/MIJN_POST_ID.
exports.posts = async function posts (app, { posts, comments, login }) {
  app.get('/posts/:id', async (req, res) => {
    const token = req.session.token;
    const credentials = await login.authenticate(token);

    const post = await posts.get(req.params.id);
    const id = (post || {})._id;
    const postComments = await comments.get((id || '').toString());

    return res.render('post', { post, credentials, comments: postComments });
  });
};

// De route voor het maken van een comment post. Deze route is "intern" en wordt niet bezocht door gebruikers.
exports.createComment = async function createComment (app, { posts, comments, login }) {
  app.post('/posts/:id/comment', async (req, res) => {
    req.headers.Authorization = req.headers.Authorization || req.session.token;
    if (!req.headers.Authorization) {
      return res.render('error', {
        title: 'Log je eerst in.',
        subtitle: 'Klik hier om je in te loggen.',
        href: '/login',
        crendentials: {}
      });
    }

    if (!req.body.content) {
      return res.render('error', {
        title: 'Vul de inhoud van je bericht in.',
        subtitle: 'Klik hier om terug te gaan naar je post.',
        href: `/posts/${req.params.id}`
      });
    }

    const credentials = await login.authenticate(req.headers.Authorization);

    const post = await posts.get(req.params.id);
    if (!post) {
      return res.render('error', {
        title: 'Deze post is niet gevonden.',
        subtitle: 'Klik hier om terug te gaan naar de home-pagina.',
        href: `/`
      });
    }

    await comments.create({
      content: req.body.content,
      author: credentials.username,
      parentPost: req.params.id
    });

    res.redirect(`/posts/${req.params.id}`);
  });
};

// Dit is de route die gebruikers bezoeken om een nieuwe post te maken.
// Eerst komen ze dus hier. Daarna wordt er een frontend-pagina geserveerd die een verzoek maakt naar /createPost.
// Daarna worden ze weer doorgestuurd naar /posts/ID, met de ID die ze kregen van createPost. 
exports.newPost = async function newPost (app, { login }) {
  app.get('/newPost', async (req, res) => {
    const token = req.session.token;
    const credentials = await login.authenticate(token);

    res.render('newPost', { credentials });
  });
};

// De contact pagina. Lekker simpel.
exports.contact = async function contact (app, { login }) {
  app.get('/contact', async (req, res) => {
    const token = req.session.token;
    const credentials = await login.authenticate(token);

    res.render('contact', { credentials });
  });
};

// De index pagina. In deze route vangen we alle posts op van de database en renderen we die ook.
exports.index = async function index (app, { login, posts, comments }) {
  app.get('/', async (req, res) => {
    const token = req.session.token;
    const credentials = await login.authenticate(token);

    const allPosts = await Promise.all((await posts.getAll())
      .map(async post => {
        post.commentCount = await comments.get(post._id.toString()).then(r => r.length);
        return post;
      }));

    res.render('index', { credentials, posts: allPosts.sort((a, b) => b.createdAt - a.createdAt) });
  });
};

// De logout pagina. Het enige wat we doen is de sessie van de gebruiker verwijderen.
exports.logout = async function (app) {
  app.get('/logout', async (req, res) => {
    req.session.destroy(() => {
      res.render('logout', { credentials: null });
    });
  });
};

// De login route. In deze functie heb je twee routes.
// De eerste is wat gebruikers bezoeken op de inlog pagina.
// De tweede is intern gebruikt. De website maakt dan een verzoek naar dat endpoint om een sessie te krijgen.
exports.login = async function login (app, { login }) {
  app.get('/login', async (req, res) => {
    res.render('login', { credentials: null });
  });

  app.post('/login', async (req, res) => {
    if (!req.body.username || !req.body.password) {
      return res.status(400).send('Missing username password parameter');
    } else {
      login.get(req.body.username, req.body.password)
        .then(credentials => {
          if (!credentials) {
            res.render('error', {
              title: 'Inlog gegevens fout.',
              subtitle: 'Klik hier om terug te gaan naar de inlog pagina.',
              href: '/login'
            });
          } else {
            req.session.token = credentials.token;
            res.redirect('/');
          }
        })
        .catch(e => {
          log(e.stack || e.message);
          res.status(500).send(`Something went wrong: ${e.message || inspect(e.stack)}`);
        });
    }
  });
};

// Dit is een intern gebruikte route voor het aanmaken van een account.
// De website maakt dan een verzoek naar dat endpoint om een account aan te maken in de database.
exports.createAccount = async function createLogin (app, { login }) {
  app.post('/createAccount', async (req, res) => {
    if (!req.body.username || !req.body.password) {
      return res.status(400).send('Missing username or password parameter');
    } else if (await login.isUsernameTaken(req.body.username)) {
      return res.render('error', {
        title: 'Gebruikersnaam in gebruik.',
        subtitle: 'Klik hier om terug te gaan naar de inlog pagina.',
        href: '/login'
      });
    } else {
      req.body.geslacht = Object.keys(req.body).find(k => req.body[k] === 'on');
      console.log(req.body);
      login.create(req.body)
        .then(token => {
          req.session.token = token;

          res.redirect('/');
        })
        .catch(e => {
          log(e.stack || e.message);
          res.status(500).send(`Something went wrong: ${e.message || inspect(e.stack)}`);
        });
    }
  });
};
