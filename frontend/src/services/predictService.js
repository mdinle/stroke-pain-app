import axiosAuth from '@/axios-auth'

export async function predictStrokeAndPain(file) {
  const formData = new FormData()
  formData.append('file', file)

  const { data } = await axiosAuth.post('/predict', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
  })

  return data
}