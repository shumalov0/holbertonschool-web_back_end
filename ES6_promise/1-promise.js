// Only make Promise
function getResponseFromAPI() {
  return new Promise((resolve, reject) => {
    /* eslint-disable */
    if (true) {
      resolve({ tatus: 200, body: "Success" });
    } else {
      reject("The fake API is not working currently");
    }
    /* eslint-enable */
  });
}
export default getResponseFromAPI;
