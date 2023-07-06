const fastapi = (operation, url, params, success_callbak, failure_callback) => {
  // 메서드, 요청URL, 요청데이터, api호출 성공시 콜백, 실패시 콜백
  let method = operation;
  let content_type = 'application/json';
  let body = JSON.stringify(params);

  // get 호출인 경우
  let _url = import.meta.env.VITE_SERVER_URL + url;
  if (method === 'get') {
    _url += '?' + new URLSearchParams(params);
  }

  // get 호출이 아닌 경우
  let options = {
    method: method,
    headers: {
      'Content-Type': content_type,
    },
  };
  if (method !== 'get') {
    options['body'] = body;
  }

  fetch(_url, options).then((res) => {
    if (res.status === 204) {
      // No content 답변 등록 시에는 응답결과가 없어도 정상
      if (success_callbak) {
        success_callbak();
      }
      return;
    }

    res
      .json()
      .then((json) => {
        if (res.status >= 200 && res.status < 300) {
          if (success_callbak) {
            success_callbak(json);
          }
        } else {
          if (failure_callback) {
            failure_callback(json);
          } else {
            alert(JSON.stringify(json));
          }
        }
      })
      .catch((err) => {
        alert(JSON.stringify(err));
      });
  });
};

export default fastapi;
