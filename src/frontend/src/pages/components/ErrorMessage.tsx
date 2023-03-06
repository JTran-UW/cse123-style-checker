type Props = {
    label: string,
    text: string
}

export default function ErrorMessage({ label, text }: Props) {
    return (
        <section className="py-1.5 px-6">
            <h3>{ label }</h3>
            <p>{ text }</p>
        </section>
    )
}
