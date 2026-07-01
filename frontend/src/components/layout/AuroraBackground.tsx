import { motion } from "framer-motion";
import type { ReactNode } from "react";

interface AuroraBackgroundProps {
  children: ReactNode;
}

export default function AuroraBackground({
  children,
}: AuroraBackgroundProps) {
  return (
    <div className="relative min-h-screen overflow-hidden bg-[#09090B] text-white">
      {/* Purple Orb */}
      <motion.div
        animate={{
          x: [0, 80, 0],
          y: [0, -60, 0],
        }}
        transition={{
          duration: 18,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        className="absolute left-[-200px] top-[-120px] h-[500px] w-[500px] rounded-full bg-violet-500/25 blur-[140px]"
      />

      {/* Emerald Orb */}
      <motion.div
        animate={{
          x: [0, -120, 0],
          y: [0, 80, 0],
        }}
        transition={{
          duration: 22,
          repeat: Infinity,
          ease: "easeInOut",
        }}
        className="absolute bottom-[-180px] right-[-120px] h-[500px] w-[500px] rounded-full bg-emerald-500/20 blur-[160px]"
      />

      {/* Grid Overlay */}
      <div
        className="absolute inset-0 opacity-[0.05]"
        style={{
          backgroundImage: `
            linear-gradient(rgba(255,255,255,0.12) 1px, transparent 1px),
            linear-gradient(90deg, rgba(255,255,255,0.12) 1px, transparent 1px)
          `,
          backgroundSize: "48px 48px",
        }}
      />

      <div className="relative z-10">{children}</div>
    </div>
  );
}