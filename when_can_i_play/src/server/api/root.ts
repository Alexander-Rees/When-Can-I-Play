import { slotRouterouter } from "when_can_i_play/server/api/routers/slot";
import { createTRPCRouter } from "when_can_i_play/server/api/trpc";

/**
 * This is the primary router for your server.
 *
 * All routers added in /api/routers should be manually added here.
 */
export const appRouter = createTRPCRouter({
  slot: slotRouter,
});

// export type definition of API
export type AppRouter = typeof appRouter;
