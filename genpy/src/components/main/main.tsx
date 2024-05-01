import classNames from 'classnames';
import styles from './main.module.scss';

export interface MainProps {
    className?: string;
}

/**
 * This component was created using Codux's Default new component template.
 * To create custom component templates, see https://help.codux.com/kb/en/article/kb16522
 */
export const Main = ({ className }: MainProps) => {
    return (
        <div className={classNames(styles.root, className)}>
            <nav>
                <a href="/home">Home</a> | <a href="/projects">Projects</a> |{' '}
                <a href="/about">About</a> | <a href="/contact">Contact Us</a>
            </nav>
            Main
        </div>
    );
};
