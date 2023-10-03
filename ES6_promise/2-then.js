function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    if (promise === true) {
      resolve({
        status: 200,
        body: 'success',
      });
    } else {
      reject(new Error());
    }
  })
    .then(() => 'Got a response from the API');
}

export default handleResponseFromAPI;
