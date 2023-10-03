import {uploadPhoto, createUser} from "utils";

function handleProfileSignup() {
    const photoPromise = uploadPhoto();
    const userPromise = createUser();

    Promise.all([photoPromise, userPromise])
        .then(([photo, user]) => {
            console.log(`photo-${photo} ${user.firstName} ${user.lastName}`);
        })
        .catch(() => {
            console.log('Signup system offline');
        });
}