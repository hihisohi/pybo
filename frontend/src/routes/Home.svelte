<script>
  import fastapi from '../lib/api';
	import { link } from 'svelte-spa-router';

  let question_list = []
  
  function get_question_list() {
    fastapi('get', '/api/question/list', {}, (json) => {
			question_list = json
		})
  }
  
  get_question_list()
</script>

<div id="questionList" class="w-full mb-14">
  <table class="w-full border-collapse border border-slate-200">
    <tr>
      <th class="bg-gray-900 border border-gray-400 text-white p-2">제목</th>
      <th class="bg-gray-900 border border-gray-400 text-white p-2">번호</th>
      <th class="bg-gray-900 border border-gray-400 text-white p-2">작성일시</th>
    </tr>
    {#each question_list as question}
      <tr>
        <td class="p-2">{question.id}</td>
        <td class="p-2"><a use:link href="/detail/{question.id}">{question.subject}</a></td>
        <td class="p-2">{question.create_date}</td>
      </tr>
    {/each}
  </table>
</div>

<a use:link href="/question-create" class="bg-indigo-900 px-4 py-2 text-white rounded-full font-bold hover:bg-indigo-600">질문 작성</a>
