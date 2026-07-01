import type { Screenshots } from "../../types/audit";

interface Props {
  screenshots: Screenshots;
}

export default function ScreenshotGallery({
  screenshots,
}: Props) {
  return (
    <section className="mt-16">
      <h2 className="mb-8 text-3xl font-bold">
        Visual Evidence
      </h2>

      <div className="space-y-10">
        <div>
          <h3 className="mb-4 text-xl font-semibold">
            Homepage
          </h3>

          <img
            src={`http://127.0.0.1:8000${screenshots.homepage}`}
            className="rounded-2xl border border-white/10"
          />
        </div>

        <div>
          <h3 className="mb-4 text-xl font-semibold">
            Product Pages
          </h3>

          <div className="grid gap-6 md:grid-cols-4 xl:grid-cols-2">
            {screenshots.products.map((image) => (
              <img
                key={image}
                src={`http://127.0.0.1:8000${image}`}
                className="rounded-2xl border border-white/10"
              />
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}