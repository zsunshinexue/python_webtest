import request from '@/utils/request'

export function test_zx_1(data) {
  return request({
    url: 'http://127.0.0.1:8000/demo/test2/',
    method: 'get',
  });
}



export function logout(data) {
  return request({
    url: '/vue-admin-template/user/logout',
    method: 'get',
    data
  })
}
