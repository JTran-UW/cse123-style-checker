/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}"
  ],
  theme: {
    extend: {
      gridTemplateRows: {
        'main' : 'min-content auto',
      }
    },
  },
  plugins: [],
}
