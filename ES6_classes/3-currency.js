/* eslint-disable no-underscore-dangle */
export default class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }
  // Getters and setters for the attributes

  get code() {
    return this._code;
  }

  get name() {
    return this._name;
  }

  set code(code) {
    this._code = code;
  }

  set name(name) {
    this._name = name;
  }

  // Method and all that
  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}
