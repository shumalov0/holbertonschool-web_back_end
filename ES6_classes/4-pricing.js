import Currency from "./3-currency";

export default class Pricing {
  constructor(currency, amount = 0) {
    // Default parametr sonda olmalıdır
    this.amount = amount;
    this.currency = currency;
  }

  displayFullPrice() {
    const code = this.currency._code;
    const name = this.currency._name;
    const money = `${this.amount} ${name} (${code})`;

    return money;
  }

  static convertPrice(amount = 0, conversionRate = 0) {
    if (typeof amount !== "number") {
      throw new TypeError("amount must be a number"); // Xəta mesajını düzəltdim
    }

    if (typeof conversionRate !== "number") {
      throw new TypeError("conversionRate must be a number"); // Xəta mesajını düzəltdim
    }

    return amount * conversionRate;
  }

  get amount() {
    return this._amount;
  }

  set amount(value) {
    if (typeof value !== "number") {
      throw new TypeError("amount must be a number"); // Yoxlama üçün ədəd olmalıdır
    }
    this._amount = value;
  }

  get currency() {
    return this._currency;
  }

  set currency(value) {
    if (!(value instanceof Currency)) {
      throw new TypeError("currency must be a Currency"); // Düzgün növ yoxlaması
    }
    this._currency = value;
  }
}
