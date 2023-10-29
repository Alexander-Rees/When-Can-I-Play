import { createNextApiHandler } from "@trpc/server/adapters/next";

import { env } from "when_can_i_play/env.mjs";
import { appRouter } from "when_can_i_play/server/api/root";
import { createTRPCContext } from "when_can_i_play/server/api/trpc";

// export API handler
export default createNextApiHandler({
  router: appRouter,
  createContext: createTRPCContext,
  onError:
    env.NODE_ENV === "development"
      ? ({ path, error }) => {
          console.error(
            `❌ tRPC failed on ${path ?? "<no-path>"}: ${error.message}`
          );
        }
      : undefined,
});
