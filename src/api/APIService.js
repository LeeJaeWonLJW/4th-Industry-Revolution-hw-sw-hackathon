import axios from 'axios'
let apiUrl = 'http://mvp.turtlelab.io'

export class APIService {
  async register (phone, password, name, gender, age, height, weight, purpose) {
    let form = new FormData()

    form.append('phone', phone)
    form.append('password', password)
    form.append('name', name)
    form.append('gender', gender)
    form.append('age', age)
    form.append('height', height)
    form.append('weight', weight)
    form.append('purpose', purpose)

    const url = `${apiUrl}/signup`
    try {
      const response = await axios.post(url, form)
      return response.data
    } catch (e) {
      return e
    }
  }
}
