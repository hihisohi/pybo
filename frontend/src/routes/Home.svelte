<script>
  import fastapi from '../lib/api';
	import { link } from 'svelte-spa-router';
  import { page } from '../lib/store';
  import dayjs from 'dayjs'

  let question_list = []
  let size = 10
  let total = 0
  $: total_page = Math.ceil(total/size) // 반응형 변수 -> api호출로 total값이 변하면 total_page도 실시간으로 계산된다
  
  function get_question_list(_page) {
    let params = {
      page: _page,
      size: size,
    }
    fastapi('get', '/api/question/list', params, (json) => {
			question_list = json.question_list
      $page = _page
      total = json.total
		})
  }
  
  $: get_question_list($page) // 반응형 기호 $ -> 변수 뿐 아니라 함수에도 사용 가능
</script>

<div id="questionList" class="w-full mb-14">
  <table class="w-full border-collapse border border-slate-200">
    <tr>
      <th class="bg-gray-900 border border-gray-400 text-white p-2">번호</th>
      <th class="bg-gray-900 border border-gray-400 text-white p-2">제목</th>
      <th class="bg-gray-900 border border-gray-400 text-white p-2">작성일시</th>
    </tr>
    {#each question_list as question, i}
      <tr>
        <td class="p-2">{total - ($page * size) - i}</td>
        <td class="p-2">
          <a use:link href="/detail/{question.id}">{question.subject}</a>
          {#if question.answers.length > 0}
          <span>{question.answers.length}</span>
          {/if}
        </td>
        <td class="p-2">{dayjs(question.create_date).format('YYYY년 MM월 DD일 HH:mm:ss')}</td>
      </tr>
    {/each}
  </table>
  <!-- 페이징 -->
  <div>
    <button on:click="{() => get_question_list($page-1)}" disabled="{$page <= 0 && "disabled"}">이전</button>
    <ul>
      {#each Array(total_page) as _, loop_page}
      {#if loop_page >= $page-5 && loop_page <= $page+5}
        <li><button on:click="{() => get_question_list(loop_page)}" class="{loop_page === $page && 'active'}">{loop_page + 1}</button></li>
      {/if}
      {/each}
    </ul>
    <button on:click="{() => get_question_list($page+1)}" disabled="{$page >= total_page-1 && "disabled"}">다음</button>
  </div>
</div>

<a use:link href="/question-create" class="btn-primary">질문 작성</a>
