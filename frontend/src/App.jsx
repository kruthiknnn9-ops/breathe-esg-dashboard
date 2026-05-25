import { useState } from 'react'
import axios from 'axios'

function App() {

  const [file, setFile] = useState(null)
  const [message, setMessage] = useState('')

  const handleUpload = async () => {

    if (!file) {
      alert('Please select a CSV file')
      return
    }

    const formData = new FormData()

    formData.append('file', file)

    try {

      const response = await axios.post(
        'https://breathe-esg-dashboard-mdwg.onrender.com/api/upload-csv/',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        }
      )

      setMessage(response.data.message)

    } catch (error) {

      console.error(error)

      setMessage('Upload failed')
    }
  }

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">

      <div className="bg-white p-10 rounded-2xl shadow-lg w-[500px]">

        <h1 className="text-4xl font-bold text-green-700 mb-6">
          Breathe ESG Dashboard
        </h1>

        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
          className="mb-4"
        />

        <button
          onClick={handleUpload}
          className="bg-green-600 text-white px-4 py-2 rounded-lg"
        >
          Upload CSV
        </button>

        {message && (
          <p className="mt-4 text-blue-600 font-semibold">
            {message}
          </p>
        )}

      </div>

    </div>
  )
}

export default App
