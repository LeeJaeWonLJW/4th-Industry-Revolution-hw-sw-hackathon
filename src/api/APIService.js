import axios from 'axios'
let apiUrl = 'http://mvp.turtlelab.io'

export class APIService {
  async register (phone, password, name, gender, age, height, weight, purpose, duration, profile) {
    let form = new FormData()

    form.append('phone', phone)
    form.append('password', password)
    form.append('name', name)
    form.append('gender', gender)
    form.append('age', age)
    form.append('height', height)
    form.append('weight', weight)
    form.append('purpose', purpose)
    form.append('duration', duration)
    form.append('profile', profile)

    const url = `${apiUrl}/auth/signup`

    try {
      const response = await axios.post(url, form)
      return response.data
    } catch (e) {
      return e
    }
  }

  async setFlavor (flavor, accessToken) {
    let form = new FormData()
    form.append('flavor', flavor)
    const url = `${apiUrl}/user/flavor/set`
    const headers = {'Authorization': `Bearer ${accessToken}`}

    try {
      const response = await axios.post(url, form, headers)
      return response.data
    } catch (e) {
      return e
    }
  }
}
