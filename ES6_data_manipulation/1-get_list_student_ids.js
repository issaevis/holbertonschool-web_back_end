export default function getListStudentIds(array) {
  const newArray = [];

  if (Array.isArray(array)) {
    array.map((item) => {
      newArray.push(item.id);
      return newArray;
    });
  }
  return newArray;
}
