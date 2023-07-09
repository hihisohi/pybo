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

<h2>{question.subject}</h2>
<div>{dayjs(question.create_date).format('YYYY년 MM월 DD일 HH:mm:ss')}</div>
<div>
    {question.content}
</div>
<Error error={error} />
<form method="post">
    <textarea rows="15" bind:value={content}></textarea>    <!-- textarea 작성내용이 content변수와 연결되어 값을 변경할때마다 content값도 자동으로 변경됨  -->
    <input type="submit" value="답변등록" on:click="{post_answer}">
</form>

<button class="btn-primary" on:click="{() => {
    push('/')
}}">목록으로</button>

<h4>{question.answers.length}개의 답변이 있습니다.</h4>
<ul>
    {#each question.answers as answer}
        <li>{answer.content}</li>
    {/each}
</ul>