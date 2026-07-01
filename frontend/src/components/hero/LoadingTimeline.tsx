import { useEffect, useState } from "react";
import { CheckCircle2, Loader2 } from "lucide-react";
import { motion } from "framer-motion";

interface LoadingTimelineProps {
  loading: boolean;
}

const steps = [
  "Validating Shopify store",
  "Extracting homepage",
  "Discovering products",
  "Analyzing product pages",
  "Generating CRO insights",
  "Preparing report",
];

export default function LoadingTimeline({
  loading,
}: LoadingTimelineProps) {
  const [currentStep, setCurrentStep] = useState(0);

  useEffect(() => {
    if (!loading) {
      setCurrentStep(0);
      return;
    }

    const interval = setInterval(() => {
      setCurrentStep((prev) =>
        prev < steps.length - 1 ? prev + 1 : prev
      );
    }, 1200);

    return () => clearInterval(interval);
  }, [loading]);

  return (
    <motion.div
      initial={{ opacity: 0, y: 25 }}
      animate={{ opacity: 1, y: 0 }}
      className="mx-auto max-w-4xl rounded-3xl border border-white/10 bg-white/5 p-8 backdrop-blur-3xl"
    >
      <h3 className="mb-6 text-xl font-semibold text-white">
        Analyzing Store...
      </h3>

      <div className="space-y-5">
        {steps.map((step, index) => (
          <div
            key={step}
            className="flex items-center gap-4"
          >
            {index < currentStep ? (
              <CheckCircle2
                size={20}
                className="text-emerald-400"
              />
            ) : index === currentStep ? (
              <Loader2
                size={20}
                className="animate-spin text-emerald-400"
              />
            ) : (
              <div className="h-5 w-5 rounded-full border border-zinc-700" />
            )}

            <span
              className={
                index <= currentStep
                  ? "text-white"
                  : "text-zinc-500"
              }
            >
              {step}
            </span>
          </div>
        ))}
      </div>
    </motion.div>
  );
}