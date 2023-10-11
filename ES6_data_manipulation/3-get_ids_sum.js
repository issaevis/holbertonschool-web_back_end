export default function getStudentIdsSum(array) {
  return array.reduce((currSum, item) => currSum + item.id, 0);
}
