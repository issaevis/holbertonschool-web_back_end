export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeInfo = newGrades.find((grade) => grade.studentId === student.id);

      if (gradeInfo) {
        return {
          ...student,
          grade: gradeInfo.grade,
        };
      }
      return {
        ...student,
        grade: 'N/A',
      };
    });
}
