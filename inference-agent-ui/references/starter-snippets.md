# Starter Snippets

## Install Core Components

```bash
npx shadcn@latest add "https://ui.inference.sh/r/agent.json"
npx shadcn@latest add "https://ui.inference.sh/r/widgets.json"
```

## Next.js API Route (AI SDK Stream)

```ts
import { streamText } from "ai"
import { openai } from "@ai-sdk/openai"

export async function POST(req: Request) {
  const { messages } = await req.json()

  const result = streamText({
    model: openai("gpt-4.1-mini"),
    messages,
  })

  return result.toUIMessageStreamResponse()
}
```

## Client Chat Composition

```tsx
"use client"

import { useChat } from "@ai-sdk/react"
import {
  Agent,
  Thread,
  PromptInput,
  Response,
} from "@/components/ui/agent"

export function ChatSurface() {
  const { messages, input, handleInputChange, handleSubmit, status } = useChat()

  return (
    <Agent>
      <Thread>
        {messages.map((message) => (
          <Response key={message.id} message={message} />
        ))}
      </Thread>
      <PromptInput
        value={input}
        onChange={handleInputChange}
        onSubmit={handleSubmit}
        disabled={status === "streaming"}
      />
    </Agent>
  )
}
```

## Inference Runtime Transform (Optional)

```ts
import { uiTransform } from "inference"

const result = streamText({
  model,
  messages,
  experimental_transform: [
    uiTransform({
      /* runtime config */
    }),
  ],
})
```

## Tool Schema Guidance

- Use explicit JSON-schema-like argument shapes.
- Keep tool names stable and action-oriented.
- Include renderable fields that map directly to widgets (title, value, trend, status, timeframe).
