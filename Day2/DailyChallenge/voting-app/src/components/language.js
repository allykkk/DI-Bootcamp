import './language.css'

const Language = ({ language, handleClick }) => {
    return (
        <div className='language'>
            <div className='voteCount'>{language.votes}</div>
            <div className='languageName'>{language.name}</div>
            <button onClick={() => handleClick(language.name)}>Click Here</button>
        </div>
    );
}

export default Language;
