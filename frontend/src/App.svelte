<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte'
  import Detail from './routes/Detail.svelte'
  import QuestionCreate from './routes/QuestionCreate.svelte'
  import Navigation from './components/Navigation.svelte';

  const routes = {
    '/': Home,
    '/detail/:question_id': Detail,
    '/question-create': QuestionCreate,

  }

</script>

<Navigation />
<div class="container mx-auto px-5">
  <Router {routes} />
</div>