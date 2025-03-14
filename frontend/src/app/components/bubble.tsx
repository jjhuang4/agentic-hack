import React from 'react';

interface BubbleProps {
    color: string;
    text: string;
}

const Bubble: React.FC<BubbleProps> = ({ color, text }) => {
    return (
        <div className={`p-4 rounded-lg`} style={{ backgroundColor: color }}>
            <p className="text-white">{text}</p>
        </div>
    );
};

export default Bubble;