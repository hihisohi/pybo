<script>
    import fastapi from "../lib/api";
    import Error from '../components/Error.svelte'
    import { push } from "svelte-spa-router";
    import dayjs from 'dayjs'

    export let params = {}
    let question_id = params.question_id
    let question = {answers:[]}
    let content = ""
    let error = {detail:[]}
    
    // 질문 가져오기
    function get_question() {
        fastapi('get', '/api/question/detail/' + question_id, {}, (json) => {
            question = json
        })
    }
    get_question()

    // 답변 달기
    function post_answer(e) {
        e.preventDefault()

        let url = "/api/answer/create/" + question_id
        let params = {
            content: content
        }

        fastapi('post', url, params, 
            (json) => {
                // 답변등록 성공시 답변창 비우고 질문 다시 조회
                content = ''
                error = {detail:[]}
                get_question()
            },
            (err_json) => {
                error = err_json
            }
        )
    }
    


</script>
<div class="deatil-header border-b pb-6">
    <h2 class="text-3xl font-bold mb-6">{question.subject}</h2>
    <div>{dayjs(question.create_date).format('YYYY년 MM월 DD일 HH:mm:ss')}</div>
</div>
<div class="deatil-body mb-6 py-12 border-b">
    <div>
        {question.content}
    </div>
    <Error error={error} />
</div>
<div class="deatil-footer">
    <button class="block btn-primary mr-0 ml-auto" on:click="{() => {
        push('/')
    }}">목록으로</button>
    <h4 class="text-lg font-bold mb-6">답변 <span class="text-indigo-500">{question.answers.length}</span></h4>
    <form method="post" class="w-full mb-10">
        <textarea rows="6" bind:value={content} class="w-full border resize-none mb-4" placeholder="답변을 작성해주세요"></textarea>    <!-- textarea 작성내용이 content변수와 연결되어 값을 변경할때마다 content값도 자동으로 변경됨  -->
        <input type="submit" value="답변 등록" on:click="{post_answer}" class="btn-submit block mr-0 ml-auto">
    </form>
    <ul>
        {#each question.answers as answer}
            <li class="border-t py-6">{answer.content}</li>
        {/each}
    </ul>
</div>

