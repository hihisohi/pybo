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
  <table class="table-fixed w-full border-collapse border-y border-gray-300">
    <tr>
      <th class="w-2/12 p-2 text-left">번호</th>
      <th class="w-6/12 p-2 text-left">제목</th>
      <th class="w-4/12 p-2 text-left">작성일시</th>
    </tr>
    {#each question_list as question, i}
      <tr class="border-t border-gray-300">
        <td class="py-4 px-2">{total - ($page * size) - i}</td>
        <td class="py-4 px-2">
          <a use:link href="/detail/{question.id}">{question.subject}</a>
          {#if question.answers.length > 0}
          <span>{question.answers.length}</span>
          {/if}
        </td>
        <td class="py-4 px-2">{dayjs(question.create_date).format('YYYY년 MM월 DD일 HH:mm:ss')}</td>
      </tr>
    {/each}
  </table>
  <!-- 페이징 -->
  <div class="relative flex justify-center mt-10">
    {#if $page > 0}
    <button on:click="{() => get_question_list($page-1)}" class="absolute inset-y-1/2 left-0 translate-y-toCenter px-2 h-8 rounded-md border text-sm">이전 페이지</button>
    {/if}
    
    <ul class="flex">
      {#if Math.floor($page/10) * 10 !== 0}
      <li><button on:click="{() => get_question_list(0)}" class="btn-paging">1</button></li>
      <li><button on:click="{() => get_question_list((Math.floor($page/10) - 1) *10)}" class="btn-paging">...</button></li>
      {/if}

      {#each Array(total_page) as _, loop_page}
      {#if loop_page >= Math.floor($page/10) * 10 && loop_page <= Math.floor($page/10) * 10 + 9}
      <li><button on:click="{() => get_question_list(loop_page)}" class="btn-paging {loop_page === $page && 'bg-indigo-600 text-white'}">{loop_page + 1}</button></li>
      {/if}
      {/each}

      {#if total_page > 10 && Math.floor($page/10) * 10 !== Math.floor(total_page/10) * 10}
      <li><button on:click="{() => get_question_list((Math.floor($page/10) + 1) *10)}" class="btn-paging">...</button></li>
      {/if}
    </ul>

    {#if $page < total_page - 1}
    <button on:click="{() => get_question_list($page+1)}" class="absolute inset-y-1/2 right-0 translate-y-toCenter px-2 h-8 rounded-md border text-sm">다음 페이지</button>
    {/if}
    
  </div>
</div>

<a use:link href="/question-create" class="btn-primary mr-auto ml-0">질문 작성</a>
