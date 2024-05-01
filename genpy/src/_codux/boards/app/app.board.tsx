import { createBoard } from '@wixc3/react-board';
import App from '../../../App';

export default createBoard({
    name: 'Auth',
    Board: () => <App />,
    isSnippet: true,
    environmentProps: {
        windowBackgroundColor: '#f4f4f4',
    },
});
