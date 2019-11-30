import axios from 'axios'
import { jwtJsDecode, jwtDecode } from 'jwt-js-decode'

const apiUrl = 'http://foodiet.pangwoon.com'

export class APIService {
	async userInfo() {
		let accessToken = localStorage.accessToken
		let jwt = jwtDecode(accessToken)

		return jwt
	}

	async login (phone, password) {
		let form = new FormData()

    form.append('email', phone)
		form.append('password', password)

		const url = `${apiUrl}/auth/signin`

		try {
			const response = await axios.post(url, form)
			if(response.data.success == true) {
				localStorage.accessToken = response.data.accessToken
				axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.accessToken}`
			}

			return response.data
		} catch (e) {
			return e
		}
	}

  async register (phone, password, name, gender, age, height, weight, goal_weight, purpose, duration, profile) {
    let form = new FormData()

    form.append('email', phone)
    form.append('password', password)
    form.append('name', name)
    form.append('gender', gender)
    form.append('age', age)
    form.append('height', height)
    form.append('weight', weight)
		form.append('goal_weight', goal_weight)
		form.append('purpose', purpose)
    form.append('duration', duration)
    form.append('profile', profile)

    const url = `${apiUrl}/auth/signup`

    try {
			const response = await axios.post(url, form)
			if(response.data.success == true) {
				localStorage.accessToken = response.data.accessToken
				axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.accessToken}`
			}

      return response.data
    } catch (e) {
      return e
    }
  }

  async setFlavor (flavor) {
    let form = new FormData()
		form.append('favorite', flavor)
		
		const url = `${apiUrl}/ai/food/add`
		axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.accessToken}`

    try {
      const response = await axios.post(url, form)
      return response.data
    } catch (e) {
      return e
    }
	}
	
	async friendSearch (phone) {
		let form = new FormData()
		form.append('email', phone)

		const url = `${apiUrl}/user/friend/search`
		axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.accessToken}`

		try {
			const res = await axios.post(url, form)
			return res.data
		} catch (e) {
			return e
		}
	}

	async friendAdd (phone) {
		let form = new FormData()
		form.append('email', phone)

		const url = `${apiUrl}/user/friend/add`
		axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.accessToken}`

		try {
			const res = await axios.post(url, form)
			return res.data
		} catch (e) {
			return e
		}
	}

	async friendList() {
		const url = `${apiUrl}/user/friend/lookup`
		axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.accessToken}`

		try {
			const res = await axios.get(url)
			return res.data
		} catch (e) {
			return e
		}
	}

	async get_todayNutrient() {
		let form = new FormData()

		const url = `${apiUrl}/nutrient/today/lookup`
		axios.defaults.headers.common['Authorization'] = `Bearer ${localStorage.accessToken}`

		try {
			const res = await axios.post(url, form)
			return res.data
		} catch (e) {
			return e
		}
	}
	
}
