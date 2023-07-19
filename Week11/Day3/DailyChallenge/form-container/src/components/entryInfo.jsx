const EntryInfo = ({ formData }) => {
  return (
    <div className="entered-info">
      <h2>Entered information:</h2>
      <p>
        Your name: {formData.firstName} {formData.lastName}
      </p>
      <p>Your age: {formData.age}</p>
      <p>Your gender: {formData.gender}</p>
      <p>Your destination: {formData.destination}</p>
      <p>Your dietary restrictions: </p>
      <div className="restrictions">
        <span>**Nuts free : {formData.nutsFree ? "Yes" : "No"}</span> <br />
        <span>**Lactose free : {formData.lactoseFree ? "Yes" : "No"}</span>{" "}
        <br />
        <span>**Vegan meal : {formData.isVegan ? "Yes" : "No"}</span>
      </div>
    </div>
  );
};

export default EntryInfo;
