<script>
    import { link } from 'svelte-spa-router'
</script>

<div id="header" class="px-12 py-4 flex">
    <a use:link href="/" class="text-xl font-bold text-indigo-500 mr-10">Pybo</a>
    <nav>
        <ul class="flex">
            <li class="px-4"><a use:link href="/" class="">회원가입</a></li>
            <li class="px-4"><a use:link href="/" class="">로그인</a></li>
        </ul>
    </nav>
</div>
