import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  let reject = {};
  const p = await signUpUser(firstName, lastName);
  const resolved = { status: 'fulfilled', value: { ...p } };
  try {
    /*eslint-disable */
    let Prom2 = await uploadPhoto(fileName);
  } catch (e) {
    reject = { status: 'rejected', value: e.toString() };
  }
  return new Promise((resolve=>resolve([resolved, reject])));
}
