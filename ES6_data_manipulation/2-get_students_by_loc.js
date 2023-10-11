export default function getStudentsByLocation(array, location) {
  const newArray = [];

  array.filter((item) => {
    if (item.location === location) {
      newArray.push(item);
    }
    return null;
  });
  return newArray;
}
