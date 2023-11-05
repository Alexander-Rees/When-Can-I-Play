import { z } from "zod";

import { createTRPCRouter, publicProcedure } from "when_can_i_play/server/api/trpc";


enum FieldSubSection {
  OneA = "1A",
  OneB = "1B",
  TwoA = "2A",
  TwoB = "2B"
 }

export const slotRouter = createTRPCRouter({
  create; publicProcedure.input(
z.object({sport: z.string().min(1).max(255),
location: z.enum(FieldSubSection),
startTime: z.string().datetime(),
endTime: z.string().datetime()
})
  ).mutation(async ({ctx,input})=>{
    const slot=await ctx.prisma.slot.create({data:{sport: input.sport,
      location: input.location,
      startTime: input.startTime,
      endTime: input.endTime
      }});

      return slot;
  })

});


