import { useState, useEffect } from 'react'

import MainSection from './components/MainSection'
import ErrorMessage from './components/ErrorMessage'

const API_URL = "http://127.0.0.1:8000"

interface Error {
  line: number,
  col: number,
  type: string,
  message: string,
  full_message: string
}

export default function Home() {
  const [errorMessages, setErrorMessages] = useState<React.ReactNode[]>([]);
  const [userCode, setUserCode] = useState<string>("");

  async function updateErrorMessages() {
    if (userCode.trim().length == 0) {
      setErrorMessages(
        [<ErrorMessage label="No code in editor" text="Start writing on the right panel" />]
      );
    } else {

      await fetch(API_URL, {
        method: "POST",
        headers: {
          "Content-Type" : "application/json"
        },
        body: JSON.stringify({
          text: userCode
        })
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.detail) {
            setErrorMessages([
              <ErrorMessage label="Invalid input!" text="Your code could not be parsed" />
            ]);
          } else if (data.errors.length == 0) {
            setErrorMessages([
              <ErrorMessage label="No Errors Found!" text="Your code looks good." />
            ]);
          } else {
            let messages: React.ReactNode[] = [];

            data.errors.forEach((message: Error) => {
              messages.push(
                <ErrorMessage
                  label={message.type + " Error at " + message.line + ":" + message.col}
                  text={message.message}
                />
              );
            });

            setErrorMessages(messages);
          }
        })
    }
  }

  function updateUserCode(event: React.ChangeEvent<HTMLTextAreaElement>) {
    setUserCode(event.target.value);
  }

  return (
    <>
      <div className="grid grid-cols-2 grid-rows-main min-h-screen">
        <MainSection
          styles="justify-self-center border-b-0 py-2.5 col-span-2 text-center"
          content={
            <h1>CSE 123 Style Checker</h1>
          }
        />

        <MainSection
          styles="flex flex-col border-r-0"
          content={
            <>
              <h2 className="py-1.5 px-6">Errors</h2>

              <section>{ errorMessages }</section>
            </>
          }
        />

        <MainSection
          styles="flex flex-col"
          content={
            <>
              <textarea
                className="outline-none resize-none rounded-none m-0 w-full box-border h-full b-0"
                onChange={ updateUserCode }></textarea>
              <button
                className="border-black border-t-4 bg-white outline-none w-full p-5 cursor-pointer text-xl font-semibold"
                onClick={ updateErrorMessages }>
                  Run
              </button>
            </>
          }
        />
      </div>
    </>
  )
}
