import { useEffect } from "react";
import { Link } from "react-router-dom"
import { useUserProfile } from "../context/UserProfile"

export default function Onboard() {
    const { userProfile } = useUserProfile();
    useEffect(() => {
        console.log(userProfile);
    }, [])
    return (
        <div>
            <h1>Hello {userProfile.username} 👋 </h1>
            {userProfile?.account !== '' ? (
                <div>                    
                    <Link to="/explore"><button className="primary"> Explore</button></Link>
                </div>
            ) : (<Link to="/register">
                <button className="primary">Join the Space! </button>
            </Link>)
            }
        </div>
    )
}