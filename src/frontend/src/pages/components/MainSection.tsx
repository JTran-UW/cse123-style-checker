type Props = {
    styles: string,
    content: React.ReactNode
}

export default function MainSection({ styles, content }: Props) {
    return (
        <section className={"border-black border-4 box-border w-full " + styles}>
            { content }
        </section>
    )
}