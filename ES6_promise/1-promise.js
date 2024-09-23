function getFullResponseFromAPI() {
  return new Promise((resolve, reject) => {
    if (resolve) {
      status: 200;
      body: "Success";
    } else {
      ("The fake API is not working currently");
    }
  });
}

export default getFullResponseFromAPI;
