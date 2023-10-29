import { type AppType } from "next/app";

import { api } from "when_can_i_play/utils/api";

import "when_can_i_play/styles/globals.css";

const MyApp: AppType = ({ Component, pageProps }) => {
  return <Component {...pageProps} />;
};

export default api.withTRPC(MyApp);
