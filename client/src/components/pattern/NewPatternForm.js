import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { object, string, number } from "yup";
import { useFormik } from "formik";
import toast from "react-hot-toast";

const NewPatternForm = () => {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editForm, setEditForm] = useState(false);
  const navigate = useNavigate();
 
const patternSchema = object({
  title: string()
    .max(50, "Title cannot be longer than 50 characters")
    .required("Title is required"),
  description: string().max(
    250,
    "Description cannot be longer than 250 characters"
  ),
  price: number(),
  author: string(),
  difficulty: string(),
});

const initialValues = {
  title: "",
  description: "",
  price: "",
  author: "",
  difficulty: "",
};

  const formik = useFormik({
    initialValues,
    validationSchema: patternSchema,
    onSubmit: (formData) => {
      setIsSubmitting(true);
      fetch("/patterns", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      })
        .then((resp) => {
          if (resp.ok) {
            navigate("/");
          } else {
            return resp.json().then((error) => {
              toast.error(error.message);
            });
          }
        })
        .catch((error) => {
          toast.error("An error occurred. Please try again.");
        })
        .finally(() => {
          setIsSubmitting(false);
        });
    },
  });

  const toggleForm = () => {
    setEditForm((prevForm) => !prevForm);
  };


  return (
    <div>
      <button onClick={toggleForm}>{editForm ? "Cancel" : "Add a Pattern"}</button>
      {editForm && (
        <form onSubmit={formik.handleSubmit}>
            <label htmlFor="title">Title</label>
            <input
            type="text"
            name="title"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.title}
            />
            {formik.errors.title && formik.touched.title && (
            <div className="error-message show">{formik.errors.title}</div>
            )}

            <label>Description</label>
            <input
            type="text"
            name="description"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.description}
            />
            {formik.errors.description && formik.touched.description && (
            <div className="error-message show">{formik.errors.description}</div>
            )}

            <label>Price</label>
            <input
            type="number"
            name="price"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.price}
            />

            <label>Author</label>
            <input
            type="text"
            name="author"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.author}
            />

            <label>Difficulty</label>
            <input
            type="text"
            name="difficulty"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.difficulty}
            />
            {formik.errors.difficulty && formik.touched.difficulty && (
            <div className="error-message show">{formik.errors.difficulty}</div>
            )}

            <button type="submit" disabled={isSubmitting}>
            Submit
            </button>
        </form>
      )}
    </div>
  );
};

export default NewPatternForm;
