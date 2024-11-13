import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FeedList = () => {
    const [feeds, setFeeds] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchFeeds = async () => {
            try {
                const response = await axios.get('http://127.0.0.1:8000/feeds/'); // Adjust the URL if needed
                setFeeds(response.data);
            } catch (error) {
                console.error('Error fetching feeds:', error);
            } finally {
                setLoading(false);
            }
        };
        fetchFeeds();
    }, []);

    if (loading) return <div>Loading...</div>;

    return (
        <div className="container">
            <h1>Your Feeds</h1>
            <ul className="list-group">
                {feeds.map(feed => (
                    <li key={feed.id} className="list-group-item">
                        <strong>{feed.platform}</strong>: {feed.content}
                        <p>{new Date(feed.timestamp).toLocaleString()}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default FeedList;
