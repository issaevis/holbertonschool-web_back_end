import { signUpUser } from './4-user-promise';
import { uploadPhoto } from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const userPromise = signUpUser(firstName, lastName);
  const photoPromise = uploadPhoto(fileName);

  return Promise.allSettled([userPromise, photoPromise]).then((results) => [
    {
      status: results[0].status,
      value: results[0].status === 'fulfilled' ? { firstName, lastName } : results[0].reason,
    },
    {
      status: results[1].status,
      value: results[1].status === 'fulfilled' ? null : results[1].reason,
    },
  ]);
}
