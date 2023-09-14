export default function appendToEachArrayValue(array, appendString) {
  const newArray = array.map(word => appendString + word);

  return newArray;
}
