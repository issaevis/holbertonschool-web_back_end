export default function createEmployeesObject(departmentName, employees) {
  const person = {};
  person[departmentName] = employees;

  return person;
}
