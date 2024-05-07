import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { object, string, number } from "yup";
import { useFormik } from "formik";
import toast from "react-hot-toast";

const NewPatternForm = () => {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [editForm, setEditForm] = useState(false);
  const [categories, setCategories] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch("/categories")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setCategories(data);
      })
      .catch((error) => {
        console.error("Error fetching categories:", error);
      });
  }, []);

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
    category_id: number().required("Category is required"),
  });

  const initialValues = {
    title: "",
    description: "",
    price: "",
    author: "",
    difficulty: "",
    type: "",
    category_id: "",
  };

  const formik = useFormik({
    initialValues,
    validationSchema: patternSchema,
    onSubmit: (formData) => {
      console.log(formData);
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
            console.log(formData);
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
    <div className="pattern-form-page">
      <div className="pattern-form-body">
        <div className="pattern-form-container">
          <button className="button-55" onClick={toggleForm}>
            {editForm ? "Cancel" : "Add a Pattern"}
          </button>
          {editForm && (
            <form id="patternForm" onSubmit={formik.handleSubmit}>
              <h2 className="new-pattern-banner">Add a new pattern!</h2>
              <label htmlFor="title">Title</label>
              <input
                type="text"
                name="title"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.title}
                className="pattern-input"
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
                className="pattern-input"
              />
              {formik.errors.description && formik.touched.description && (
                <div className="error-message show">
                  {formik.errors.description}
                </div>
              )}

              <label>Category</label>
              <select
                name="category_id" // Use category_id instead of category_name
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.category_id}
                className="pattern-input"
              >
                <option value="">Select a category</option>
                {categories.map((category) => (
                  <option key={category.id} value={category.id}>
                    {category.name}
                  </option>
                ))}
              </select>
              {formik.errors.category_id && formik.touched.category_id && (
                <div className="error-message show">
                  {formik.errors.category_id}
                </div>
              )}

              {/* <label>Price</label>
              <input
                type="number"
                name="price"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.price}
                className="pattern-input"
              /> */}

              <label>Is Free?</label>
              <select
                name="is_free"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.is_free}
                className="pattern-input"
              >
                <option value="false">No</option>
                <option value="true">Yes</option>
              </select>

              {!formik.values.is_free && (
                <div>
                  <label>Price</label>
                  <input
                    type="number"
                    name="price"
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    value={formik.values.price}
                    className="pattern-input"
                  />
                  {formik.errors.price && formik.touched.price && (
                    <div className="error-message show">
                      {formik.errors.price}
                    </div>
                  )}
                </div>
              )}

              <label>Author</label>
              <input
                type="text"
                name="author"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.author}
                className="pattern-input"
              />

              <label>Type</label>
              <select
                name="type"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.type}
                className="pattern-input"
              >
                <option value="">Select type</option>
                <option value="Knit">Knit</option>
                <option value="Crochet">Crochet</option>
              </select>
              {formik.errors.type && formik.touched.type && (
                <div className="error-message show">{formik.errors.type}</div>
              )}

              <label>Difficulty</label>
              <input
                type="text"
                name="difficulty"
                onChange={formik.handleChange}
                onBlur={formik.handleBlur}
                value={formik.values.difficulty}
                className="pattern-input"
              />
              {formik.errors.difficulty && formik.touched.difficulty && (
                <div className="error-message show">
                  {formik.errors.difficulty}
                </div>
              )}

              <button
                className="button-55-1"
                type="submit"
                disabled={isSubmitting}
              >
                Submit
              </button>
            </form>
          )}
        </div>
      </div>
    </div>
  );
};

export default NewPatternForm;
