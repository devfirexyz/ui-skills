# ui.inference.sh Capability Map

## What It Is

- A shadcn/ui component registry focused on agent chat UIs.
- Core component set includes `Agent`, `Thread`, `PromptInput`, `Message`, `MessageContent`, `Response`, and `Tool`.
- Widget packs exist for structured outputs like weather, finance, and chart-like cards.

## What It Is Not

- Not a full backend or orchestration framework by itself.
- Not tied to one model provider if your backend emits AI SDK-compatible UI message streams.
- Not an automatic replacement for your app's state management, auth, or persistence.

## Integration Modes

1. `generic-stream`
- Use with any backend that returns AI SDK stream protocol responses.
- Use for Next.js App Router API routes, server actions, or external agent runtimes with compatible stream output.

2. `inference-runtime`
- Use inference runtime APIs and add `uiTransform`.
- Best when the model should generate widget payloads directly from tool outputs.

## Registry Bundles

- `https://ui.inference.sh/r/agent.json`: core chat/agent primitives.
- `https://ui.inference.sh/r/widgets.json`: widget component set.
- `https://ui.inference.sh/r/actions.json`: action UI primitives.
- `https://ui.inference.sh/r/citations.json`: inline citation cards.
- `https://ui.inference.sh/r/sources.json`: source cards and badges.

## Tooling Model

- Server tools:
  - Execute on backend.
  - Preferred for data access and privileged operations.
- Client tools:
  - Execute in browser.
  - Use for local side effects and instant UI interactions.

## Minimum Environment Expectations

- React application with Tailwind (registry output assumes utility classes).
- shadcn CLI available for component install.
- AI SDK-compatible chat route and streaming response.
