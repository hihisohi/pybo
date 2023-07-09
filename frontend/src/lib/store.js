import { writable } from 'svelte/store';

// 그냥 store는 새로고침 시 초기화되는 문제가 있음 -> store가 지속성을 가질 수 있게 localStorage를 활용
const persist_storage = (key, initValue) => {
  const storedValueStr = localStorage.getItem(key);
  const store = writable(storedValueStr != null ? JSON.parse(storedValueStr) : initValue);

  // subscribe() : store의 값이 변경될때 실행되는 콜백함수
  store.subscribe((val) => {
    localStorage.setItem(key, JSON.stringify(val));
  });
  return store;
};

export const page = persist_storage('page', 0);
