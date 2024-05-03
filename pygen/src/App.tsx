import { Button, Card, Form, Menu, Checkbox } from 'semantic-ui-react';
import styles from './App.module.scss';

function App() {
    return (
        <div>
            <div className={styles.page}>
                <Form style={{ gridColumn: '2' }}>
                    <Form.Field>
                        <label>Username</label>
                        <input placeholder="Username" />
                    </Form.Field>
                    <Form.Field>
                        <label>Password</label>
                        <input placeholder="Password" />
                    </Form.Field>
                    <Form.Field>
                        <Checkbox label="remember me" />
                    </Form.Field>
                    <Button type="submit">Submit</Button>
                </Form>
            </div>
        </div>
    );
}

export default App;
