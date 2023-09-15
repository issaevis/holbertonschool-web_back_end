// eslint-disable-next-line import/extensions
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const classRoomArray = [];
  classRoomArray.push(new ClassRoom(19));
  classRoomArray.push(new ClassRoom(20));
  classRoomArray.push(new ClassRoom(34));

  return classRoomArray;
}
